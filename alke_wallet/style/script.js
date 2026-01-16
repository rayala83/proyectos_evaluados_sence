$(document).ready(function() {
    $('#login').on('submit', function(event) {
        event.preventDefault(); 

        const email = $('#email').val();
        const password = $('#password').val();

       
        if (email === 'email@email.com' && password === '12345') {
            alert('Inicio de sesión exitoso');
            window.location.href = 'menu.html';
        } else {
            alert('Credenciales incorrectas, intente nuevamente');
        }
    });
});

$(document).ready(function() {
    
    
    function cargarSaldo() {
        const saldoGuardado = localStorage.getItem('saldoCuenta') || '0';
        $('#saldo-cuenta').text('$' + saldoGuardado);
    }

    
    $('.btn-redirect, .btn-secondary').on('click', function() {
        const url = $(this).data('url');
        const destino = url.replace('.html', '');

        if (url) {
            alert('Redirigiendo a: ' + destino);
            window.location.href = url;
        }
    });

    
    cargarSaldo();

   
    $(window).on('storage', function() {
        cargarSaldo();
    });
});

$(document).ready(function() {
    
    $('#form-deposito').on('submit', function(event) {
        event.preventDefault(); 

        const $inputMonto = $('#monto-deposito');
        const valorASumar = parseFloat($inputMonto.val());

        if (!isNaN(valorASumar) && valorASumar > 0) {
           
            let saldoActual = parseFloat(localStorage.getItem('saldoCuenta')) || 0;
            
            
            let nuevoSaldo = saldoActual + valorASumar;
            
           
            localStorage.setItem('saldoCuenta', nuevoSaldo);
            
          
            registrarMovimiento('Depósito', valorASumar, 'Carga de saldo en cuenta');

          
            alert('¡Depósito de $' + valorASumar.toLocaleString('es-CL') + ' realizado con éxito!');
            $inputMonto.val('');
            
            
            window.location.href = 'menu.html';
            
        } else {
            alert('Por favor, ingresa una cantidad válida.');
        }
    });

    function registrarMovimiento(tipo, monto, detalle) {
        let historial = JSON.parse(localStorage.getItem('historialMovimientos')) || [];
        
        const nuevoMovimiento = {
            tipo: tipo,
            monto: monto, 
            detalle: detalle,
            fecha: new Date().toLocaleString()
        };
        
        historial.unshift(nuevoMovimiento);
        localStorage.setItem('historialMovimientos', JSON.stringify(historial));
    }
});

$(document).ready(function() {
    const SALDO_KEY = 'saldoCuenta';
    const USUARIOS = [
        { id: 'John Doe', nombre: 'John Doe', alias: 'john.doe' },
        { id: 'Jane Smith', nombre: 'Jane Smith', alias: 'jane.smith' },
        { id: 'Charlie Brown', nombre: 'Charlie Brown', alias: 'charlie.b' }
    ];

    function cargarSaldoActual() {
        const saldo = parseFloat(localStorage.getItem(SALDO_KEY)) || 0;
        $('#saldoActualDisplay').text('$' + saldo.toLocaleString('es-CL'));
    }

    function llenarSelector() {
        const $select = $('#destinatario');
        USUARIOS.forEach(u => {
            $select.append(`<option value="${u.id}">${u.nombre} (${u.alias})</option>`);
        });
    }

    
    $('#formTransferencia').on('submit', function(e) {
        e.preventDefault();

        const destinatario = $('#destinatario').val();
        const monto = parseFloat($('#monto').val());
        let saldoActual = parseFloat(localStorage.getItem(SALDO_KEY)) || 0;

        if (saldoActual >= monto) {
            saldoActual -= monto;
            localStorage.setItem(SALDO_KEY, saldoActual);
            
            
            registrarMovimiento('Transferencia', monto, `Enviado a ${destinatario}`);

            alert(`¡Transferencia de $${monto.toLocaleString('es-CL')} enviada con éxito!`);
            window.location.href = 'menu.html';
        } else {
            alert("Saldo insuficiente.");
        }
    });

    function registrarMovimiento(tipo, monto, detalle) {
        let historial = JSON.parse(localStorage.getItem('historialMovimientos')) || [];
        historial.unshift({
            tipo: tipo,
            monto: monto,
            detalle: detalle,
            fecha: new Date().toLocaleString()
        });
        localStorage.setItem('historialMovimientos', JSON.stringify(historial));
    }

   
    $('#formNuevoContacto').on('submit', function(e) {
        e.preventDefault();
        alert("Contacto guardado exitosamente (simulación)");
        $('#modalContacto').modal('hide'); 
    });

    
    cargarSaldoActual();
    llenarSelector();
});

$(document).ready(function() {
    
    function cargarMovimientos() {
        const $lista = $('#listaMovimientos');
        const $mensajeVacio = $('#mensajeVacio');
        
        // Obtener historial
        const historial = JSON.parse(localStorage.getItem('historialMovimientos')) || [];

        if (historial.length === 0) {
            $mensajeVacio.show();
            return;
        }

        $mensajeVacio.hide();
        $lista.empty(); 

        historial.forEach(mov => {
            
            const esDeposito = mov.tipo.includes('Depósito');
            const colorClase = esDeposito ? 'text-success' : 'text-danger';
            const signo = esDeposito ? '+' : '-';
            
           
            const montoFormateado = parseFloat(mov.monto).toLocaleString('es-CL');

            const itemHtml = `
                <li class="list-group-item d-flex justify-content-between align-items-center bg-transparent py-3">
                    <div>
                        <div class="fw-bold">${mov.tipo}</div>
                        <small class="text-muted d-block">${mov.detalle}</small>
                        <small class="text-muted italic" style="font-size: 0.75rem;">${mov.fecha}</small>
                    </div>
                    <span class="fw-bold ${colorClase}" style="font-size: 1.1rem;">
                        ${signo} $${montoFormateado}
                    </span>
                </li>
            `;
            $lista.append(itemHtml);
        });
    }

   
    $('#btn-limpiar').on('click', function() {
        if (confirm("¿Estás seguro de que deseas borrar todo el historial de movimientos?")) {
            localStorage.removeItem('historialMovimientos');
            cargarMovimientos();
            location.reload();
        }
    });

    
    cargarMovimientos();
});