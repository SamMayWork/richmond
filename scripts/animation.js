document.addEventListener('DOMContentLoaded', () => {
  setTimeout(() => {
    document.querySelector('.lettercontainer').scrollIntoView({
      behavior : 'smooth'
    })
  }, 1000);
});