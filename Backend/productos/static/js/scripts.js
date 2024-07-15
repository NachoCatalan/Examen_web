document.addEventListener('DOMContentLoaded', function () {
    document.getElementById('contactForm').addEventListener('submit', function (event) {
        event.preventDefault();

        const nombre = document.getElementById('id_nombre_completo').value;
        const email = document.getElementById('id_correo').value;
        const telefono = document.getElementById('id_telefono').value;
        const moneda = document.getElementById('id_tipo_moneda').value;

        if (!nombre || !email || !telefono || !moneda) {
            alert("Todos los campos son obligatorios.");
            return;
        }

        if (!validateEmail(email)) {
            alert("Por favor, introduce un correo electrónico válido.");
            return;
        }

        // Aquí envías el formulario de manera asíncrona
        this.submit(); // Envía el formulario
    });

    document.getElementById('id_telefono').addEventListener('input', function () {
        this.value = this.value.replace(/[^0-9]/g, '');
    });

    document.getElementById('id_nombre_completo').addEventListener('input', function () {
        this.value = this.value.replace(/[^a-zA-Z\s]/g, '');
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(email);
    }
});

document.addEventListener('DOMContentLoaded', function () {
    const buttons = document.querySelectorAll('.btn-transition');

    buttons.forEach(button => {
        button.addEventListener('click', function (event) {
            event.preventDefault(); 
            const originalText = this.textContent;
            this.textContent = 'Producto añadido!';
            this.classList.add('added');

            setTimeout(() => {
                this.textContent = originalText;
                this.classList.remove('added');
                window.location.href = this.href;
            }, 3000);
        });
    });
});




document.addEventListener('DOMContentLoaded', function () {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    const carritoLista = document.getElementById('carrito-lista');
    const vaciarCarritoBtn = document.getElementById('vaciar-carrito');

    function mostrarCarrito() {
        carritoLista.innerHTML = '';
        carrito.forEach((producto, index) => {
            const li = document.createElement('li');
            li.className = 'list-group-item d-flex justify-content-between align-items-center';
            li.innerHTML = `
                ${producto.nombre} - $${producto.precio}
                <button class="btn btn-danger btn-sm" onclick="eliminarProducto(${index})">Eliminar</button>
            `;
            carritoLista.appendChild(li);
        });
    }

    function eliminarProducto(index) {
        carrito.splice(index, 1);
        localStorage.setItem('carrito', JSON.stringify(carrito));
        mostrarCarrito();
    }

    vaciarCarritoBtn.addEventListener('click', function () {
        localStorage.removeItem('carrito');
        mostrarCarrito();
    });

    mostrarCarrito();

    window.eliminarProducto = eliminarProducto;
});


function agregarAlCarrito(nombre, precio) {
    const carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.push({ nombre, precio });
    localStorage.setItem('carrito', JSON.stringify(carrito));
    alert('Producto añadido al carrito');
}

document.querySelectorAll('.btn-agregar-carrito').forEach(button => {
    button.addEventListener('click', function () {
        const nombre = this.getAttribute('data-nombre');
        const precio = this.getAttribute('data-precio');
        agregarAlCarrito(nombre, precio);
    });
});



