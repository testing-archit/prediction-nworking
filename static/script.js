document.getElementById('predict-btn').addEventListener('click', function() {
    const ticker = document.getElementById('ticker').value;
    
    fetch(`/predict?ticker=${ticker}`)
        .then(response => response.json())
        .then(data => {
            const predictedPrices = data.prices;
            const predictedPricesList = document.getElementById('predicted-prices');
            predictedPricesList.innerHTML = '';

            predictedPrices.forEach(price => {
                const li = document.createElement('li');
                li.textContent = `Predicted Price: ${price}`;
                predictedPricesList.appendChild(li);
            });
        })
        .catch(error => {
            console.error('Error:', error);
        });
});
