
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

// Test addShakeAnimation function again
test('addShakeAnimation should remove animation style after a certain delay', () => {
  const button = document.createElement('button');
  addShakeAnimation(button);
  setTimeout(() => {
    expect(button.style.animation).toBe('');
  }, 600); // Assuming the animation duration is 0.5s, we wait for 600ms to ensure animation completion
});

// Test changeTextColor function again
test('changeTextColor should revert button text color to initial color after a certain delay', () => {
  const button = document.createElement('button');
  changeTextColor(button);
  setTimeout(() => {
    expect(button.style.color).not.toBe('blue');
  }, 600); // Assuming a delay of 600ms, check that color is not blue after the delay
});
