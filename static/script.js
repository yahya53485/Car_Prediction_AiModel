 const brandModels = {
      "Audi": ["A3", "A4", "A6", "Q3", "Q5"],
      "Bentley": ["Continental GT", "Flying Spur", "Bentayga"],
      "BMW": ["X1", "X3", "X5", "Z4"],
      "Datsun": ["Go", "Redi-GO"],
      "Ferrari": ["488", "F8", "Roma"],
      "Force": ["Trax", "One"],
      "Ford": ["EcoSport", "Endeavour", "Figo"],
      "Honda": ["City", "Amaze", "Jazz", "WR-V"],
      "Hyundai": ["i20", "Creta", "Venue", "Verna", "Grand i10"],
      "Isuzu": ["D-Max", "MU-X"],
      "Jaguar": ["F-Pace", "XE", "XF"],
      "Jeep": ["Compass", "Wrangler"],
      "Kia": ["Seltos", "Sonet", "Carnival"],
      "Land Rover": ["Range Rover", "Discovery", "Evoque"],
      "Lexus": ["NX", "RX", "ES"],
      "Mahindra": ["Thar", "XUV300", "Bolero"],
      "Maruti": ["Swift", "Baleno", "Wagon R", "Brezza", "Dzire"],
      "Maserati": ["Ghibli", "Levante", "Quattroporte"],
      "Mercedes-AMG": ["A 45", "C 63", "E 63"],
      "Mercedes-Benz": ["A-Class", "C-Class", "E-Class", "S-Class"],
      "MG": ["Hector", "Zs EV", "Astor"],
      "Mini": ["Cooper", "Countryman"],
      "Nissan": ["Kicks", "Magnite", "Terrano"],
      "Porsche": ["911", "Cayenne", "Macan"],
      "Renault": ["Kwid", "Duster", "Triber"],
      "Rolls-Royce": ["Phantom", "Cullinan", "Ghost"],
      "Skoda": ["Octavia", "Superb", "Kushaq"],
      "Tata": ["Nexon", "Harrier", "Safari"],
      "Toyota": ["Innova", "Fortuner", "Glanza", "Yaris"],
      "Volkswagen": ["Polo", "Virtus", "Tiguan"],
      "Volvo": ["XC40", "XC60", "XC90"]
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