['e', 'f', 'j', 'i'].forEach(key => {
    Mousetrap.bind(key, () => {
        console.log(key)
    }, 'keydown');
    // Mousetrap.bind(key, () => {
    //     keysDown[key] = false;
    //     switchOff(keyDirections[key]);
    // }, 'keyup');
});