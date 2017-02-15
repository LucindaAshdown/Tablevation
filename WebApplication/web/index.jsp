<%-- 
    Document   : index
    Created on : Feb 11, 2017, 5:37:59 PM
    Author     : Jamie
    Author     : Nota
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>

<html>

    <head>
        <title>Tablevation - Home</title>
        <meta charset="utf-8">
        <meta name="description" content="">
        <meta name="author" content="Jamie Toloui">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- Bootstrap core CSS -->
        <link href="css/bootstrap.min.css" rel="stylesheet">

        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <link href="css/ie10-viewport-bug-workaround.css" rel="stylesheet">
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/css/bootstrap-select.min.css">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
        <link href="css/carousel.css" rel="stylesheet">

        <!-- Favicon -->
        <link rel="apple-touch-icon" sizes="57x57" href="img/favicon/apple-icon-57x57.png">
        <link rel="apple-touch-icon" sizes="60x60" href="img/favicon/apple-icon-60x60.png">
        <link rel="apple-touch-icon" sizes="72x72" href="img/favicon/apple-icon-72x72.png">
        <link rel="apple-touch-icon" sizes="76x76" href="img/favicon/apple-icon-76x76.png">
        <link rel="apple-touch-icon" sizes="114x114" href="img/favicon/apple-icon-114x114.png">
        <link rel="apple-touch-icon" sizes="120x120" href="img/favicon/apple-icon-120x120.png">
        <link rel="apple-touch-icon" sizes="144x144" href="img/favicon/apple-icon-144x144.png">
        <link rel="apple-touch-icon" sizes="152x152" href="img/favicon/apple-icon-152x152.png">
        <link rel="apple-touch-icon" sizes="180x180" href="img/favicon/apple-icon-180x180.png">
        <link rel="icon" type="image/png" sizes="192x192" href="img/favicon/android-icon-192x192.png">
        <link rel="icon" type="image/png" sizes="32x32" href="img/favicon/favicon-32x32.png">
        <link rel="icon" type="image/png" sizes="96x96" href="img/favicon/favicon-96x96.png">
        <link rel="icon" type="image/png" sizes="16x16" href="img/favicon/favicon-16x16.png">
        <link rel="manifest" href="img/favicon/manifest.json">
        <meta name="msapplication-TileColor" content="#ffffff">
        <meta name="msapplication-TileImage" content="img/favicon/ms-icon-144x144.png">
        <meta name="theme-color" content="#ffffff">
    </head>

    <body>
        <div class="navbar-wrapper">
            <div class="container">

                <nav class="navbar navbar-default">
                    <div class="container-fluid">
                        <!-- Brand and toggle get grouped for better mobile display -->
                        <div class="navbar-header">
                            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                                <span class="sr-only">Toggle navigation</span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                                <span class="icon-bar"></span>
                            </button>

                            <a class="navbar-brand" href="#">
                                <img alt="Tablevation logo" src="img/logo.jpg" width="90" height="30">
                            </a>

                            <a class="navbar-brand" href="#">Tablevation</a>
                        </div>

                        <!-- Collect the nav links, forms, and other content for toggling -->
                        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul class="nav navbar-nav">
                                <li class="active"><a href="index.html">Home <span class="sr-only">(current)</span></a></li>
                                    <%
                                        HttpSession sess = request.getSession();
                                        String sessEmail = (String) request.getParameter("email");
                                        if (sessEmail == null) {
                                    %>
                                <li><a href="login.html">Login</a></li>
                                <li><a href="CreateCustomerAccount.html">Create Customer Account</a></li>
                                <li><a href="CreateRestaurantAccount.html">Create Restaurant Account</a></li>
                                    <%
                                    } else {
                                    %>
                                <li class="dropdown active">
                                    <a href="CustomerSearchRestaurants.html" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Search Restaurants<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="CustomerSearchRestaurants.html">Gunwharf</a></li>
                                        <li><a href="CustomerSearchRestaurants.html">Fratton</a></li>
                                        <li><a href="CustomerSearchRestaurants.html">Southsea</a></li>
                                        <li><a href="CustomerSearchRestaurants.html">Old Portsmouth</a></li>
                                        <li><a href="CustomerSearchRestaurants.html">Eastney</a></li>
                                        <li><a href="CustomerSearchRestaurants.html">Cosham</a></li>
                                    </ul>
                                </li>
                                <li><a href="CustomerMakeBooking.html">Make Booking</a></li>
                                <li><a href="CustomerViewReservations.html">View Bookings</a></li>
                                <li><a href="CustomerAmendReservation.html">Amend Bookings</a></li>
                                <li><a href="EditCustomerAccount.html">Edit Account</a></li>
                                <li><a href="index.html">Log out</a></li>
                                    <%
                                        }
                                    %>
                                <!-- Drop dropdown code -->
                                <!-- <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">One more separated link</a></li>
              </ul>
            </li> -->
                            </ul>
                            <!-- This is the code for links on the right side of the nav bar -->
                            <!-- <ul class="nav navbar-nav navbar-right">
            <li><a href="#">Link</a></li>
            <li class="dropdown">
              <a href="#" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Dropdown <span class="caret"></span></a>
              <ul class="dropdown-menu">
                <li><a href="#">Action</a></li>
                <li><a href="#">Another action</a></li>
                <li><a href="#">Something else here</a></li>
                <li role="separator" class="divider"></li>
                <li><a href="#">Separated link</a></li>
              </ul>
            </li>
          </ul> -->
                        </div>
                        <!-- /.navbar-collapse -->
                    </div>
                    <!-- /.container-fluid -->
                </nav>

            </div>
        </div>


        <div id="myCarousel" class="carousel slide" data-ride="carousel">
            <!-- Indicators -->
            <ol class="carousel-indicators">
                <li data-target="#myCarousel" data-slide-to="0" class="active"></li>
                <li data-target="#myCarousel" data-slide-to="1"></li>
                <li data-target="#myCarousel" data-slide-to="2"></li>
            </ol>
            <div class="carousel-inner" role="listbox">
                <div class="item active">
                    <img class="first-slide" src="img/Restaurantimg.jpg" alt="First slide">
                    <div class="container">
                        <div class="carousel-caption">
                            <!--<p>Note: If you're viewing this page via a <code>file://</code> URL, the "next" and "previous" Glyphicon buttons on the left and right might not load/display properly due to web browser security rules.</p> -->
                            <%
                                if (sessEmail == null) {
                            %>  
                            <p><a class="btn btn-lg btn-primary" href="login.html" role="button">Sign up/Login today</a></p> 
                            <%
                                }
                            %>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img class="second-slide" src="img/Restaurant2img.jpg" alt="Second slide">
                    <div class="container">
                        <div class="carousel-caption">
                            <%
                                if (sessEmail == null) {
                            %>  
                            <p><a class="btn btn-lg btn-primary" href="login.html" role="button">Sign up/Login today</a></p> 
                            <%
                                }
                            %>
                        </div>
                    </div>
                </div>
                <div class="item">
                    <img class="third-slide" src="img/Restaurant3img.jpg" alt="Third slide">
                    <div class="container">
                        <div class="carousel-caption">
                            <%
                                if (sessEmail == null) {
                            %>  
                            <p><a class="btn btn-lg btn-primary" href="login.html" role="button">Sign up/Login today</a></p> 
                            <%
                                }
                            %>
                        </div>
                    </div>
                </div>
            </div>
            <a class="left carousel-control" href="#myCarousel" role="button" data-slide="prev">
                <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
                <span class="sr-only">Previous</span>
            </a>
            <a class="right carousel-control" href="#myCarousel" role="button" data-slide="next">
                <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
                <span class="sr-only">Next</span>
            </a>
        </div>
        <!-- /.carousel -->



        <!-- Marketing messaging and featurettes
      ================================================== -->
        <!-- Wrap the rest of the page in another container to center all the content. -->

        <div class="container marketing">

            <!-- Three columns of text below the carousel -->
            <div class="row">
                <%
                    String typeOfUser = (String) sess.getAttribute("type_of_user");
                    if (sessEmail != null && typeOfUser.equals("customer")) {
                %>
                <form method="post">
                    <div class="col-lg-4">
                        <img class="img-circle" src="img/food.jpg" alt="Generic placeholder image" width="140" height="140">
                        <h2>Many Locations</h2>
                        <p>Our services cater to all areas within Portsmouth. We hope to be expanding soon.</p>
                        <select class="selectpicker" name="Area" data-live-search="true" title="Please select a location" data-width="auto;">
                            <option>Gunwharf</option>
                            <option>Southsea</option>
                            <option>Fratton</option>
                            <option>Old Portsmouth</option>
                            <option>Eastney</option>
                            <option>Cosham</option>
                        </select>
                        <input type="hidden" name="action" value="select_restaurants_by_area"/>
                        <button class="btn btn-success" formaction="RestaurantController" role="button">Submit &raquo;</button>
                    </div>
                </form>
                <%
                    }
                %>
                <%
                    if (sessEmail == null) {
                %>
                <!-- /.col-lg-4 -->
                <div class="col-lg-4">
                    <img class="img-circle" src="img/restaurant_table.jpg" alt="Generic placeholder image" width="140" height="140">
                    <h2>Reserve Tables Easily</h2>
                    <p>This website makes booking tables easy. Please register or login if you would like to use our services.</p>
                    <p><a class="btn btn-default" href="login.html" role="button">Login &raquo;</a></p>
                </div>
                <!-- /.col-lg-4 -->
                <div class="col-lg-4">
                    <img class="img-circle" src="img/food3.jpg" alt="Generic placeholder image" width="140" height="140">
                    <h2>All types of Restaurants</h2>
                    <p>Every restaurant you can think of is on this website. If you are a Resaurant who would like to register, please click below.</p>
                    <p><a class="btn btn-default" href="CreateRestaurantAccount.html" role="button">Register Restaurant &raquo;</a></p>
                </div>
                <!-- /.col-lg-4 -->
                <%
                    }
                %>
            </div>
            <!-- /.row -->


            <!-- START THE FEATURETTES -->

            <!-- FOOTER -->
            <footer>
                <a name="Bottom">
                    <p class="pull-right"><a href="#">Back to top</a></p>
                    <p>Tablevation &middot; <a href="#">Privacy</a> &middot; <a href="#">Terms</a></p>
            </footer>

        </div>
        <!-- /.container -->



        <footer>

        </footer>
        <!-- Bootstrap core JavaScript
        ================================================== -->
        <!-- Placed at the end of the document so the pages load faster -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <script>
            window.jQuery || document.write('<script src="js/jquery.min.js"><\/script>')
        </script>
        <script src="js/bootstrap.min.js"></script>
        <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
        <script src="js/holder.min.js"></script>
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <script src="js/ie10-viewport-bug-workaround.js"></script>
        <!-- Latest compiled and minified JavaScript -->
        <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/js/bootstrap-select.min.js"></script>
    </body>

</html>