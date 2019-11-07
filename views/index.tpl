<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Recetas</title>

  <!-- Bootstrap core CSS -->
  <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet"
    integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">


  <style>
    .bd-placeholder-img {
      font-size: 1.125rem;
      text-anchor: middle;
      -webkit-user-select: none;
      -moz-user-select: none;
      -ms-user-select: none;
      user-select: none;
    }

    @media (min-width: 768px) {
      .bd-placeholder-img-lg {
        font-size: 3.5rem;
      }
    }
  </style>
  <!-- Custom styles for this template -->
  <link href="/style/style.css" rel="stylesheet">
</head>

<body>

  <main role="main">
  <form method="post" action="buscar_receta">
    <section class="jumbotron text-center">
      <div class="container">
        <h1 class="jumbotron-heading">Recetas</h1>
        <p class="lead text-muted">Encontrá aquí, solo con un click, todas tús recetas!</p>
        <div class="input-group mb-3">
          <input type="text" class="form-control" aria-label="Username" id='query' name="query">
        </div>
        <p>
          <button type="submit" class="btn btn-primary my-2">Buscar</button>
        </p>
      </div>
    </section>
  </form>

    <div class="album py-5 bg-light">
      <div class="container">
        <div class="row">
          

            % for rec in recetas:
            <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
              <img class="bd-placeholder-img card-img-top" width="100%" height="225" src="{{rec.image}}"
                preserveAspectRatio="xMidYMid slice" focusable="false" role="img"
                aria-label="Placeholder: Thumbnail"></img>
              <div class="card-body">
                <p class="card-text">{{rec.label}}</p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <button type="button" class="btn btn-sm btn-outline-secondary">Ver</button>
                  </div>
                  <small class="text-muted">Calorias receta: {{rec.calories}}</small>
                </div>
              </div>
            </div>
            </div>
            % end

          
        </div>
      </div>
    </div>

  </main>
</body>

</html>