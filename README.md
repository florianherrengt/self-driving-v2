docker run -it --device=/dev/mem -v $(pwd):/home --privileged -p 8000:8000 sd bash

```
udevd[7]: error: runtime directory '/run/udev' not writable, for now falling back to '/dev/.udev'
root@dee97fbe3fd8:/# udevd[20]: rename '/dev/console.udev-tmp' '/dev/console' failed: Device or resource busy
```

Flask doesn't work with python 3.2