javascript: (() => {
    const stopWhenNLeft = 10;

    const letterElement = document.getElementById('actualLetter');
    const remainingText = document.getElementById('remainingText');
    while (remainingText.textContent.length >= stopWhenNLeft) {
        let charCode = letterElement.textContent.charCodeAt(0) == 160 ? 32 : letterElement.textContent.charCodeAt(0);
        document.dispatchEvent(new KeyboardEvent('keypress', { 'keyCode': charCode }));
        document.dispatchEvent(new KeyboardEvent('keyup', { 'keyCode': charCode }));
    }
})();