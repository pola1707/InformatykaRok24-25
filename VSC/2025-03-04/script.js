let currentSlide = 0;
const slides = document.querySelectorAll('.slide');
const totalSlides = slides.length;

// Funkcja do przełączania slajdów
function moveToNextSlide() {
    // Ukrywamy obecny slajd
    slides[currentSlide].classList.remove('active');
    
    // Zwiększamy indeks slajdu
    currentSlide = (currentSlide + 1) % totalSlides;
    
    // Pokazujemy nowy slajd
    slides[currentSlide].classList.add('active');
}

// Inicjalizacja: pokazujemy pierwszy slajd
slides[currentSlide].classList.add('active');

// Ustawienie, aby slider automatycznie przesuwał się co 4 sekundy
setInterval(moveToNextSlide, 4000); // Co 4 sekundy zmienia się slajd
