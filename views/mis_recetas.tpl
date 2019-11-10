<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Mis Recetas</title>

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
  <!-- <link href="/style/style.css" rel="stylesheet"> -->
</head>

<body style="background-color:#e9ecef;">

<nav class="navbar navbar-expand-lg navbar-dark bg-primary">
  <img class="navbar-brand" src="https://icons-for-free.com/iconfiles/png/512/flat+version+svg+cutlery-1319964487059654922.png" width="55" height="65"></img>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarColor01">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item">
        <a class="nav-link" href="\index">Buscador</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="\mis_recetas">Mis Recetas <span class="sr-only">(current)</span></a>
      </li>
    </ul>
    % if usuario != None:
    <form class="form-inline my-2 my-lg-0" action="login">
      <button class="btn btn-secondary my-2 my-sm-0" type="submit">Cerrar Sesión</button>
    </form>
    % else:
    <form class="form-inline my-2 my-lg-0" action="login">
      <button class="btn btn-secondary my-2 my-sm-0" type="submit">Ingresar</button>
    </form>
    % end
  </div>
</nav>

% if recetas != []:
<section class="jumbotron">
<div class="album py-5">
      <div class="container">
        <div class="row">
          

            % for rec in recetas:
            <div class="col-md-4">
            <div class="card mb-4 shadow-sm">
            <object data="https://stackoverflow.com/does-not-exist.png" type="image/png">
              <img class="bd-placeholder-img card-img-top" width="100%" height="225" src="{{rec.image}}"
                preserveAspectRatio="xMidYMid slice" focusable="false" role="img"
                aria-label="Placeholder: Thumbnail"></img>
            </object>
              <div class="card-body">
                <p class="card-text">{{rec.label}}</p>
                <div class="d-flex justify-content-between align-items-center">
                  <div class="btn-group">
                    <form action={{rec.url}}>
                      <button type="submit" class="btn btn-sm btn-outline-secondary">Ver</button>
                    </form>
                    % if rec.favorite == True:
                    <form action={{rec.url}}>
                      <img hspace="10" src="https://cdn2.iconfinder.com/data/icons/color-svg-vector-icons-part-2/512/dating_eating_vector_icon-512.png" width="30" height="30"/>
                    </form>
                    % else:
                    <form action={{rec.url}}>
                      <img hspace="10" src="https://cdn1.iconfinder.com/data/icons/circle-outlines/512/Like_Favourite_Love_Health_Heart_Favourites_Favorite-512.png" width="30" height="30"/>
                    </form>
                    % end
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
</section>
% end
  </main>
</body>

</html>