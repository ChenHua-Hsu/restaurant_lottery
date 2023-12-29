let isImage = true;

function toggleImage() {
  const image = document.getElementById('image');

  if (isImage) {
    image.src = 'templates/shake.gif';
  } else {
    image.src = 'templates/ok.png';
  }

  isImage = !isImage;
}