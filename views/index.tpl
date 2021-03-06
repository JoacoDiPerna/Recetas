<!doctype html>
<html lang="en">

<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

<script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
<script>
% if usuario != None:
var id_usuario = {{usuario.id_usuario}}
% end
 function agregar_favoritos(img) {
  var uri = document.getElementById(img.id).getAttribute('data-uri');
  var label = document.getElementById(img.id).getAttribute('data-label');
  document.getElementById(img.id).src = "https://cdn2.iconfinder.com/data/icons/color-svg-vector-icons-part-2/512/dating_eating_vector_icon-512.png";
  document.getElementById(img.id).setAttribute("onclick", "quitar_favoritos(this);");
  $.ajax({
    type: "POST", 
    data: JSON.stringify({'id_usuario': id_usuario, "uri": uri, "label": label}),
    url: "/grabar_receta_favorita" ,
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    });
  }
  function quitar_favoritos(img) {
  var uri = document.getElementById(img.id).getAttribute('data-uri');
  var label = document.getElementById(img.id).getAttribute('data-label');
    document.getElementById(img.id).src = "https://cdn1.iconfinder.com/data/icons/circle-outlines/512/Like_Favourite_Love_Health_Heart_Favourites_Favorite-512.png";
    document.getElementById(img.id).setAttribute("onclick","agregar_favoritos(this);");
      $.ajax({
    type: "POST", 
    data: JSON.stringify({'id_usuario': id_usuario, "uri": uri, "label": label}),
    url: "/borrar_receta_favorita" ,
    contentType: "application/json; charset=utf-8",
    dataType: "json",
    });
  }
</script>

<title>Buscador</title>

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
background-color: #e9ecef;
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
<li class="nav-item active">
  <a class="nav-link" href="\index">Buscador <span class="sr-only">(current)</span></a>
</li>
% if usuario != None: 
<li class="nav-item">
  <a class="nav-link" href="\mis_recetas">Mis Recetas</a>
</li>
% end
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

<main role="main">
  <form method="post" action="\index">
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
                    % if usuario != None:
                      % if rec.favorite == True:
                      <form action={{rec.url}}>
                        <img hspace="10" src="https://cdn2.iconfinder.com/data/icons/color-svg-vector-icons-part-2/512/dating_eating_vector_icon-512.png" width="30" height="30" id="{{rec.uri}}{{rec.label}}" onclick="quitar_favoritos(this);" data-uri="{{rec.uri}}" data-label="{{rec.label}}"/>
                      </form>
                      % else:
                      <form action={{rec.url}}>
                        <img hspace="10" src="https://cdn1.iconfinder.com/data/icons/circle-outlines/512/Like_Favourite_Love_Health_Heart_Favourites_Favorite-512.png" width="30" height="30" id="{{rec.uri}}{{rec.label}}" onclick="agregar_favoritos(this);" data-uri="{{rec.uri}}" data-label="{{rec.label}}"/>
                      </form>
                      % end
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