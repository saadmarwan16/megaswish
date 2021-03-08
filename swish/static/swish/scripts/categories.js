document.querySelectorAll('.product-image').forEach(image => {
        
    image.addEventListener('mousemove', event => {

        let width = image.offsetWidth;
        let height = image.offsetHeight;
        let mouseX = event.offsetX;
        let mouseY = event.offsetY;

        let bgPosX = (mouseX / width * 100);
        let bgPosY = (mouseY / height * 100);

        image.style.backgroundPosition = `${bgPosX}% ${bgPosY}%`;
    })

    image.addEventListener('mouseleave', () => {

        image.style.backgroundPosition = 'center';
    })
})