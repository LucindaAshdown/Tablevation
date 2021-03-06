<%-- 
    Document   : RestaurantViewReservations
    Created on : Feb 16, 2017, 3:45:00 PM
    Author     : Nota
    Author     : Jamie
--%>

<%@page import="java.util.Calendar"%>
<%@page import="java.util.Date"%>
<%@page import="model.ReservationModel"%>
<%@page import="java.util.LinkedList"%>
<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html>

<head>
    <title>Tablevation - View Reservation</title>
    <meta charset="utf-8">
    <meta name="description" content="">
    <meta name="author" content="Jamie Toloui">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css/Searchmenu.css" rel="stylesheet">
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
                            <li><a href="RestaurantMenu.html">Menu</a></li>
                            <li class="active"><a href="RestaurantViewReservations.html">View Reservations <span class="sr-only">(current)</span></a></li>
                            <li><a href="RestaurantUpdateReservations.html">Update Reservations</a></li>
                            <li><a href="EditRestaurantAccount.html">Edit Account</a></li>
                            <li><a href="Controller?action=logout">Log out</a></li>
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

    <!-- Content Section -->
    <section>
      <div class="container">
          <h1>Current Bookings</h1>

          <div class="row">
              <div class="row">
                      <%
                        LinkedList<ReservationModel> reservationList = (LinkedList<ReservationModel>) request.getAttribute("reservationList");
                        int length = reservationList.size();
                        for(int i = 0; i < length;i++){
                            ReservationModel reservation = reservationList.get(i);
                            Date bookedDate = reservation.getBookedDate();
                            Calendar cal = Calendar.getInstance();
                            cal.setTime(bookedDate);
                            int year = cal.get(Calendar.YEAR);
                            int month = cal.get(Calendar.MONTH) + 1;
                            int day = cal.get(Calendar.DAY_OF_MONTH);
                            int hours = cal.get(Calendar.HOUR_OF_DAY);
                            int minutes = cal.get(Calendar.MINUTE);
                            String bookedDateString = day + "/" + month + "/" + year + " " + hours + ":" + minutes;
                            String customerEmail = reservation.getCustomerEmail();
                            int numberOfGuests = reservation.getNumberOfGuests();
                            String details = reservation.getDetails();
                      %>
                  <div class="col-sm-4">
                      <!-- here starts the box that hold restaurant name and description -->
                      <label>booking date and time:<%=bookedDateString%></label>
                      <p>customer email:<%=customerEmail%></p>
                      <p>number of guests:<%=numberOfGuests%></p>
                      <%
                          if(details != null){ 
                      %>
                      <p>additional details:<%=details%></p>
                      <%
                       }
                      %>
                  </div>
                      <%
                        }
                      %>
                  <!-- here ends the box that hold restaurant name and description -->
              </div>
          </div>
      </div>
    </section>



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

