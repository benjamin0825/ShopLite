// Submit the cart quantity form as soon as the quantity changes.
document.querySelectorAll("form.js-auto-submit select").forEach((select) => {
  select.addEventListener("change", () => select.form.submit());
});
