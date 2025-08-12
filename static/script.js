 const brandModels = {
      "Hyundai": ["i20", "Creta", "Venue", "Verna", "Grand i10"],
      "Maruti": ["Swift", "Baleno", "Wagon R", "Brezza", "Dzire"],
      "Toyota": ["Innova", "Fortuner", "Glanza", "Yaris"],
      "Honda": ["City", "Amaze", "Jazz", "WR-V"],
      "Kia": ["Seltos", "Sonet", "Carnival"]
    };

    const brandSelect = document.getElementById('brand');
    const modelSelect = document.getElementById('model');

    brandSelect.addEventListener('change', function() {
      const brand = this.value;
      modelSelect.innerHTML = '<option value="">-- Select Model --</option>';
      if (brandModels[brand]) {
        brandModels[brand].forEach(model => {
          const opt = document.createElement('option');
          opt.value = model;
          opt.textContent = model;
          modelSelect.appendChild(opt);
        });
      }
    });