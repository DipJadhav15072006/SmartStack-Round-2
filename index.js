 const minSlider = document.getElementById("minRange");
  const maxSlider = document.getElementById("maxRange");
  const minOutput = document.getElementById("minVal");
  const maxOutput = document.getElementById("maxVal");

  function updateValues() {
    const min = parseInt(minSlider.value);
    const max = parseInt(maxSlider.value);
    if (min > max) {
      minSlider.value = max;
    }
    minOutput.textContent = minSlider.value;
    maxOutput.textContent = maxSlider.value;
  }

  minSlider.oninput = updateValues;
  maxSlider.oninput = updateValues;

  updateValues();