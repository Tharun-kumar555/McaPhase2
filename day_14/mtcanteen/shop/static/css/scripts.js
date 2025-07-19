// Dropdown menu hover for touch devices (optional)
document.addEventListener('DOMContentLoaded', () => {
  const dropdowns = document.querySelectorAll('.dropdown');

  dropdowns.forEach(dropdown => {
    const trigger = dropdown.querySelector('a');

    // Toggle dropdown on click for touch devices
    trigger.addEventListener('click', (e) => {
      e.preventDefault();
      dropdown.classList.toggle('open');
    });
  });

  // Close dropdowns if clicked outside
  document.addEventListener('click', (e) => {
    dropdowns.forEach(dropdown => {
      if (!dropdown.contains(e.target)) {
        dropdown.classList.remove('open');
      }
    });
  });
});

// Optional: Alert when item added to cart (for feedback)
const addToCartButtons = document.querySelectorAll('a[href*="add-to-cart"]');
addToCartButtons.forEach(btn => {
  btn.addEventListener('click', (e) => {
    // Optional: You can show a popup instead of redirect if using AJAX
    alert('Item added to cart!');
  });
});
