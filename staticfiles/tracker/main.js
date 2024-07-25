const ctx = document.getElementById('cryptoChart').getContext('2d');
const selectElement = document.getElementById('crypto-select');
let chart;
let selectedCrypto = 'btcusdt';

// Function to fetch available cryptocurrencies
async function fetchCryptoList() {
    try {
        const response = await fetch('http://localhost:8000/get-symbols/');
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching crypto list:', error);
        return [];
    }
}

// Function to populate the dropdown
async function populateDropdown() {
    const cryptoList = await fetchCryptoList();
    cryptoList.forEach(crypto => {
        const option = document.createElement('option');
        option.value = crypto.symbol.toLowerCase();
        option.textContent = `${crypto.name} (${crypto.symbol})`;
        selectElement.appendChild(option);
    });
    selectElement.addEventListener('change', (event) => {
        selectedCrypto = event.target.value;
        updateChart();
    });
}

// Function to fetch data from the API
async function fetchCryptoData(symbol) {
    try {
        const response = await fetch(`http://localhost:8000/latest-day-data/${symbol}/?format=json`);
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error fetching data:', error);
        return [];
    }
}

async function updateChart() {
    const data = await fetchCryptoData(selectedCrypto);
    if (data.length === 0) return;

    const labels = data.map(item => new Date(item.created_at).toLocaleTimeString());
    const prices = data.map(item => item.price);

    if (chart) {
        chart.data.labels = labels;
        chart.data.datasets[0].data = prices;
        chart.data.datasets[0].label = `${selectedCrypto.toUpperCase()} Price`;
        chart.update();
    } else {
        chart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: `${selectedCrypto.toUpperCase()} Price`,
                    data: prices,
                    borderColor: 'rgb(75, 192, 192)',
                    tension: 0.1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    x: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Time'
                        }
                    },
                    y: {
                        display: true,
                        title: {
                            display: true,
                            text: 'Price (USDT)'
                        }
                    }
                }
            }
        });
    }
}

// Initialize the page
async function init() {
    await populateDropdown();
    await updateChart();
    setInterval(updateChart, 10000); // Update every 10 seconds
}

init();