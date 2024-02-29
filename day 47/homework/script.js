let balance = 0;

    function updateBalance(amount) {
      const balanceElement = document.getElementById('balance');
      balance += amount;
      balanceElement.textContent = balance;
    }

    function deposit() {
      const amountInput = document.getElementById('amount');
      const amount = parseFloat(amountInput.value);
      if (!isNaN(amount) && amount > 0) {
        updateBalance(amount);
      } else {
        alert('Please enter a valid amount to deposit.');
      }
      amountInput.value = '';
    }

    function withdraw() {
      const amountInput = document.getElementById('amount');
      const amount = parseFloat(amountInput.value);
      if (!isNaN(amount) && amount > 0 && amount <= balance) {
        updateBalance(-amount);
      } else {
        alert('Please enter a valid amount to withdraw.');
      }
      amountInput.value = '';
    }