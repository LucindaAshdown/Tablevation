<%-- 
    Document   : CustomerMenu
    Created on : Feb 16, 2017, 5:48:43 PM
    Author     : Nota
    Author     : Jamie
--%>
    
<%@page import="model.RestaurantModel"%>
<%@page import="java.util.LinkedList"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>
    
<!DOCTYPE html>
<html>
    
    <head>
        <title>Tablevation - Menu</title>
        <meta charset="utf-8">
        <meta name="description" content="">
        <meta name="author" content="Jamie Toloui">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link href="css/Customermenu.css" rel="stylesheet">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
        <script src="js/jquery.js"></script>
            
        <!-- Custom CSS -->
        <link href="css/full-width-pics.css" rel="stylesheet">
            
        <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
            <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
            <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
        <![endif]-->
        <!-- Bootstrap core CSS -->
        <link href="css/bootstrap.min.css" rel="stylesheet">
            
        <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
        <link href="css/ie10-viewport-bug-workaround.css" rel="stylesheet">
        <!-- Latest compiled and minified CSS -->
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/css/bootstrap-select.min.css">
            
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
                                
                            <a class="navbar-brand" href="index.html">Tablevation</a>
                        </div>
                            
                        <!-- Collect the nav links, forms, and other content for toggling -->
                        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                            <ul class="nav navbar-nav">
                                <li class="active"><a href="CustomerMenu.jsp">Menu <span class="sr-only">(current)</span></a></li>
                                <!-- Drop dropdown code -->
                                <li class="dropdown">
                                    <a href="CustomerSearchRestaurants.html" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Search Restaurants<span class="caret"></span></a>
                                    <ul class="dropdown-menu">
                                        <li><a href="CustomerController?action=select_restaurants_by_area&Area=gunwharf">Gunwharf</a></li>
                                        <li><a href="CustomerController?action=select_restaurants_by_area&Area=fratton">Fratton</a></li>
                                        <li><a href="CustomerController?action=select_restaurants_by_area&Area=southsea">Southsea</a></li>
                                        <li><a href="CustomerController?action=select_restaurants_by_area&Area=old_portsmouth">Old Portsmouth</a></li>
                                        <li><a href="CustomerController?action=select_restaurants_by_area&Area=eastney">Eastney</a></li>
                                        <li><a href="CustomerController?action=select_restaurants_by_area&Area=cosham">Cosham</a></li>
                                    </ul>
                                </li>
                                <li><a href="CustomerController?action=select_reservations">View Bookings</a></li>
                                <li><a href="EditCustomerAccount.html">Edit Account</a></li>
                                <li><a href="Controller?action=logout">Log out</a></li>
                            </ul>
                        </div>
                        <!-- /.navbar-collapse -->
                    </div>
                    <!-- /.container-fluid -->
                </nav>
                    
                    
                    
            </div>
        </div>
            
        <!-- Full Width Image Header with Logo -->
        <!-- Image backgrounds are set within the full-width-pics.css file. -->
        <header class="image-bg-fluid-height">
            <img class="img-responsive img-center" src="img/logo.jpg" alt="Logo">
        </header>
            
        <!-- Content Section -->
        <section>
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <h1 class="section-heading">Menu</h1>
                        <p class="lead section-lead">click on your chosen restaurant to view their menu.</p>
                        <p class="section-paragraph">Enjoy internationally or national inspired dishes. Brunch / Lunch / afternoon teas / Sunday Lunch / Dessert / Sunday Roast.</p>
                    </div>
                </div>
            </div>
        </section>
            
        <div class="container">
            <h1>Location Name</h1>
            <div class="row">
                <div class="row">
                    
                        <%
                            LinkedList<RestaurantModel> restaurantsByArea = (LinkedList<RestaurantModel>) request.getAttribute("restaurantList");
                            if(restaurantsByArea != null){
                              int length = restaurantsByArea.size();
                              for(int i = 0; i< length; i++){
                                RestaurantModel restaurant = restaurantsByArea.get(i);
                                String name = restaurant.getName();
                                String foodType = restaurant.getFoodType();
                                String addressLine1 = restaurant.getAddressLine1();
                                String contactNumber = restaurant.getContactNumber();
                                String restaurantEmail = restaurant.getEmail();
                                String postCode = restaurant.getPostCode();
                        %>    
                        <div class="col-sm-4">
                        <!-- here starts the box that hold restaurant name and description -->
                        <label><%=name%></label>
                            
                        <p class="menu_description">
                            Food type:<%=foodType%><br>
                            Address:<%=addressLine1%><br>
                            Contact number:<%=contactNumber%><br>
                            Contact number:<%=postCode%><br>
                        </p>
                        <a class="btn btn-success"
                           href="CustomerController?action=reservation_page&Restaurant_Email=<%=restaurantEmail%>&Restaurant_Name=<%=name%>"
                           role="button">
                            Book a table
                        </a>
                    </div>
                        <%
                               }
                            }
                        %>
                    <!-- here ends the box that hold restaurant name and description -->
                </div>
                    
                    
            </div>
        </div>
            
        <!-- Content Section -->
            
            
        <!-- Footer -->
        <footer>
            <div class="container">
                <div class="row">
                    <div class="col-lg-12">
                        <p>Copyright &copy; Tablevation 2017</p>
                    </div>
                </div>
                <!-- /.row -->
            </div>
            <!-- /.container -->
        </footer>
            
        <!-- jQuery -->
        <script src="js/jquery.js"></script>
            
        <!-- Bootstrap Core JavaScript -->
        <script src="js/bootstrap.min.js"></script>
            
    </body>
        
</html>