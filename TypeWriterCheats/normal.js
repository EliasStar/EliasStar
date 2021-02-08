javascript: (() => {
    const msBetweenPresses = 100;
    const stopWhenNLeft = 10;

    const letterElement = document.getElementById('actualLetter');
    const remainingText = document.getElementById('remainingText');
    const loop = setInterval(() => {
        let charCode = letterElement.textContent.charCodeAt(0) == 160 ? 32 : letterElement.textContent.charCodeAt(0);
        document.dispatchEvent(new KeyboardEvent('keypress', { 'keyCode': charCode }));
        document.dispatchEvent(new KeyboardEvent('keyup', { 'keyCode': charCode }));
        if (remainingText.textContent.length <= stopWhenNLeft) clearInterval(loop);
    }, msBetweenPresses);
})();