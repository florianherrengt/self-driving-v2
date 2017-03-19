import RPi.GPIO as GPIO
import atexit
from http import server
import socketserver
from urllib.parse import urlparse, parse_qs

left_forward = 17
left_backward = 27
left_speed = 18

right_forward = 22
right_backward = 24
right_speed = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

left_pins = [left_forward, left_backward, left_speed]
right_pins = [right_forward, right_backward, right_speed]
all_pins = left_pins + right_pins

GPIO.setup(all_pins, GPIO.OUT)
GPIO.output(all_pins, GPIO.LOW)

left_pwm = GPIO.PWM(left_speed, 100)
right_pwm = GPIO.PWM(right_speed, 100)
left_pwm.start(0)
right_pwm.start(0)


def exit_handler():
    GPIO.output(all_pins, GPIO.LOW)
    GPIO.cleanup()


def set_movement(enabled, side, direction, percent):
    try:
        pwm = left_pwm if direction == 'left' else right_pwm
        pwm.ChangeDutyCycle(percent)
        if side == 'left':
            GPIO.output(left_pins, GPIO.LOW)
        else:
            GPIO.output(right_pins, GPIO.LOW)
        if direction == 'forward':
            pin = left_forward if side == 'left' else right_forward
        else:
            pin = left_backward if side == 'left' else right_backward
        status = GPIO.HIGH if enabled else GPIO.LOW
        GPIO.output(pin, status)
    except ValueError:
        print(ValueError)
        exit_handler()


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        if url.path != '/':
            self.send_response(200)
            self.end_headers()
            return
        query = parse_qs(url.query)
        direction = query['direction'][0]
        side = query['side'][0]
        enabled = query['enabled'][0] == 'true'
        speed = int(query['speed'][0])
        content = 'direction: {}\n'\
            'side: {}\n'\
            'enabled: {}\n'\
            'speed: {}'.format(direction, side, enabled, speed).encode('utf-8')
        self.send_response(200)
        self.send_header('Age', 0)
        self.send_header('Cache-Control', 'no-cache, private')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(content))
        self.end_headers()
        set_movement(enabled, side, direction, speed)
        self.wfile.write(content)


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True


address = ('0.0.0.0', 8000)
server = StreamingServer(address, StreamingHandler)
server.serve_forever()

atexit.register(exit_handler)
