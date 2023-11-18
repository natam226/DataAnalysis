<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $host = "localhost";
    $user = "root";
    $pass = "";
    $db = "basedatoszaga";
    $con = mysqli_connect($host, $user, $pass, $db) or die("Error en la conexión con el servidor");

    $fecha = date('Y-m-d', strtotime($_POST["Fecha"]));
    $nombreCliente = mysqli_real_escape_string($con, $_POST["Nombre"]);
    $apellidoCliente = mysqli_real_escape_string($con, $_POST["Apellido_del_Cliente"]);
    $cc = mysqli_real_escape_string($con, $_POST["Cedula_de_ciudadania_del_cliente"]);
    $convenio = mysqli_real_escape_string($con, $_POST["Convenio"]);
    $sexo = mysqli_real_escape_string($con, $_POST["Sexo"]);
    $monto = mysqli_real_escape_string($con, $_POST["Monto"]);
    $asesor = mysqli_real_escape_string($con, $_POST["Asesor"]);
    $estadoCredito = mysqli_real_escape_string($con, $_POST["Estado"]);
    $entidad = mysqli_real_escape_string($con, $_POST["Entidad"]);

    $stmt = $con->prepare("INSERT INTO `gestion datos zaga` (Fecha, NombreCliente, apellidoCliente, CC, Convenio, Sexo, Monto, Asesor, `Estado de credito`, Entidad)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)");

    $stmt->bind_param("ssssssdsss", $fecha, $nombreCliente, $apellidoCliente, $cc, $convenio, $sexo, $monto, $asesor, $estadoCredito, $entidad);

    if ($stmt->execute()) {
        echo "Los datos se han insertado correctamente.<br>";

        echo "Valores enviados desde el formulario:<br>";
        foreach ($_POST as $nombre => $valor) {
            echo "$nombre: $valor<br>";
        }

        echo '<a href="index.html"><button>Volver al Index</button></a>';
    } else {
        echo "Error al insertar los datos: " . $stmt->error . "<br>";
    }
    $stmt->close();
    mysqli_close($con);
}
?>

