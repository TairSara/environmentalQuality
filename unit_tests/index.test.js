// Import the functions you want to test
const { addShakeAnimation, changeTextColor } = require('./script');

// Test addShakeAnimation function
test('addShakeAnimation should set button animation style', () => {
  const button = document.createElement('button');
  addShakeAnimation(button);
  expect(button.style.animation).toBe('shake 0.5s');
});

// Test changeTextColor function
test('changeTextColor should set button text color to blue', () => {
  const button = document.createElement('button');
  changeTextColor(button);
  expect(button.style.color).toBe('blue');
});
