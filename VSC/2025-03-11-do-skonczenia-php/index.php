<!DOCTYPE html>
<html lang="pl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>kalkulator :3</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link rel="stylesheet" href="style.css">
</head>

<body>
    <header class="header text-center">
        <h1>Nowoczesna Strona</h1>
    </header>

    <div class="container mt-4">
        <div class="row">
            <nav class="col-md-3 menu">
                <ul class="list-group">
                    <li class="list-group-item"><a href="index.php?id=link1" class="text-decoration-none">Link 1</a></li>
                    <li class="list-group-item"><a href="index.php?id=link2" class="text-decoration-none">Link 2</a></li>
                    <li class="list-group-item"><a href="index.php?id=link3" class="text-decoration-none">Link 3</a></li>
                </ul>
            </nav>
            <main class="col-md-9 content">
                <?php
                $id = isset($_GET['id']) ? $_GET['id'] : "";

                switch($id){
                    case "link1": include 'link1.php'; break;
                    case "link2": include 'link2.php'; break;
                    case "link3": include 'link3.php'; break;
                    default: include 'default.php'; break;
                }
                ?>
            </main>
        </div>
    </div>

    <footer class="footer text-center">
        <p>&copy; 2025 Nowoczesna Strona. Wszelkie prawa zastrzeżone.</p>
    </footer>

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>

</html> 