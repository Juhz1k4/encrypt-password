document.getElementById('encryptBtn').addEventListener('click', async () => {
    const password = document.getElementById('password').value;
    if (!password) {
        alert('Por favor, digite uma senha!');
        return;
    }

    const response = await fetch('http://127.0.0.1:5000/encrypt', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ password }),
    });

    const data = await response.json();
    const resultDiv = document.getElementById('result');
    resultDiv.innerHTML = `
        <p>Senha Criptografada: <b>${data.encrypted}</b></p>
        <p class="${data.strength}">Força da Senha: ${data.strength.toUpperCase()}</p>
        <p class="message">${data.message}</p>
    `;
});
