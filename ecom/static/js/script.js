const bar = document.getElementById('bar');
const close = document.getElementById('close');
const nav = document.getElementById('navbar');

// navbar
if (bar) {
    bar.addEventListener('click', () => {
        nav.classList.add('active');
    })
}

if (close) {
    close.addEventListener('click', () => {
        nav.classList.remove('active');
    })
}

// added to cart alert
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
        var messageContainer = document.getElementById('message-container');
        if (messageContainer) {
            messageContainer.style.display = 'none';
        }
    }, 1400);
});

// stripe 
document.addEventListener("DOMContentLoaded", function () {
    const stripe = Stripe(STRIPE_PUBLISHABLE_KEY); // The variable is passed dynamically in HTML

    const checkoutButton = document.getElementById("checkout-button");

    checkoutButton.addEventListener("click", () => {
        fetch("/create-checkout-session/")
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    console.error("Error:", data.error);
                } else {
                    stripe.redirectToCheckout({ sessionId: data.id });
                }
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    });
});