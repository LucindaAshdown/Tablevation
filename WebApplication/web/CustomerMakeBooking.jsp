<%-- 
    Document   : CustomerMakeBooking
    Created on : Feb 16, 2017, 6:36:00 PM
    Author     : Nota
--%>

<%@page contentType="text/html" pageEncoding="UTF-8"%>

<!DOCTYPE html>
<html lang="en">

<head>
    <title>Tablevation - Make Reservation</title>
    <meta charset="utf-8">
    <meta name="description" content="">
    <meta name="author" content="Jamie Toloui">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="css/makeBooking.css" rel="stylesheet">
    <script src="js/validatr.min.js"></script>
    <script src="js/jquery.js"></script>

    <!-- Bootstrap stylesheet -->
    <link rel="stylesheet" type="text/css" href="css/bootstrap.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.4.1/css/bootstrap-datepicker3.css" />
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/css/bootstrap-select.min.css">


    <!-- Special version of Bootstrap that only affects content wrapped in .bootstrap-iso -->
    <link rel="stylesheet" href="https://formden.com/static/cdn/bootstrap-iso.css" />
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
    <link rel="stylesheet" type="text/css" href="css/bootstrap-clockpicker.min.css">



    <!-- Inline CSS based on choices in "Settings" tab -->
    <style>
        .bootstrap-iso .formden_header h2,
        .bootstrap-iso .formden_header p,
        .bootstrap-iso form {
            font-family: Arial, Helvetica, sans-serif;
            color: black
        }

        .bootstrap-iso form button,
        .bootstrap-iso form button:hover {
            color: white !important;
        }

        .asteriskField {
            color: red;
        }
    </style>

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

                        <a class="navbar-brand" href="index.jsp">Tablevation</a>
                    </div>

                    <!-- Collect the nav links, forms, and other content for toggling -->
                    <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                        <ul class="nav navbar-nav">
                            <li><a href="CustomerMenu.jsp">Menu</a></li>

                            <!-- Drop dropdown code -->
                            <li class="dropdown">
                                <a href="CustomerSearchRestaurants.html" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">Search Restaurants<span class="caret"></span></a>
                                <ul class="dropdown-menu">
                                    <li>
                                        <a href="CustomerController?action=select_restaurants_by_area&Area=gunwharf">
                                            Gunwharf
                                        </a>
                                    </li>
                                    <li>
                                        <a href="CustomerController?action=select_restaurants_by_area&Area=fratton">
                                            Fratton
                                        </a>
                                    </li>
                                    <li>
                                        <a href="CustomerController?action=select_restaurants_by_area&Area=southsea">
                                            Southsea
                                        </a>
                                    </li>
                                    <li>
                                        <a href="CustomerController?action=select_restaurants_by_area&Area=old_portsmouth">
                                            Old portsmouth
                                        </a>
                                    </li>
                                    <li>
                                        <a href="CustomerController?action=select_restaurants_by_area&Area=eastney">
                                            Eastney
                                        </a>
                                    </li>
                                    <li>
                                        <a href="CustomerController?action=select_restaurants_by_area&Area=cosham">
                                            Cosham
                                        </a>
                                    </li>
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

    <!-- Content Section -->
    <section>
        <div class="container">
            <div class="row">
                <div class="col-lg-12">
                    <h1 class="section-heading">Make a reservation</h1>
                    <div class="module form-module">
                        <div class="toggle">
                        </div>
                        <div class="form">
                            <h2>Fill in this form to create a booking</h2>
                            <form autocomplete="on" method="post">

                                <div>
                                    <label for="Area">Please a time</label>
                                    <select class="selectpicker" type="text" name="Booked_Time" data-live-search="true" required="" title="Please a time e.g HH:MM" data-width="100%">
                                    <option value="12:00">12:00PM</option>
                                    <option value="12:30">12:30PM</option>
                                    <option value="13:00">13:00PM</option>
                                    <option value="13:30">13:30PM</option>
                                    <option value="14:00">14:00PM</option>
                                    <option value="14:30">14:30PM</option>
                                    <option value="15:00">15:00PM</option>
                                    <option value="15:30">15:30PM</option>
                                    <option value="16:00">16:00PM</option>
                                    <option value="16:30">16:30PM</option>
                                    <option value="17:00">17:00PM</option>
                                    <option value="17:30">17:30PM</option>
                                    <option value="18:00">18:00PM</option>
                                    <option value="18:30">18:30PM</option>
                                    <option value="19:30">19:30PM</option>
                                    <option value="20:00">20:00PM</option>
                                    <option value="20:30">20:30PM</option>
                                    <option value="21:00">21:00PM</option>
                                    <option value="21:30">21:30PM</option>
                                    <option value="22:00">22:00PM</option>
                                    <option value="22:30">22:30PM</option>
                                    <option value="23:00">23:00PM</option>
                                    <option value="23:30">23:30PM</option>
                                    <option value="12:00">12:00AM</option>
                                  </select>
                                </div>

                                <div>
                                    <label for="Booked_Date">Reservation date</label>
                                    <div class="input-group">
                                        <div class="input-group-addon">
                                            <i class="fa fa-calendar"></i>
                                        </div>
                                        <input class="form-control" id="date" name="Booked_Date" placeholder="MM/DD/YYYY" type="text" />
                                    </div>
                                </div>

                                <div>
                                    <label for="No_Guests">Total number of seats</label>
                                    <input type="number" min="1" max="20" name="No_Guests" value="" placeholder="Total number of guest" required="" />

                                    <div class="requirements">
                                        Restaurants seat currently must be between 1-40.
                                    </div>
                                </div>


                                <div>
                                    <label for="Details">Extra details</label>
                                    <textarea class="form-control" name="Details" rows="5" id="comment"></textarea>
                                </div>
                                <%
                                    String restaurantEmail = request.getParameter("Restaurant_Email");
                                    String restaurantName = request.getParameter("Restaurant_Name");
                                %>
                                <input type="hidden" name="Restaurant_Name" value="<%=restaurantName%>">
                                <input type="hidden" name="Restaurant_Email" value="<%=restaurantEmail%>">
                                <input type="hidden" name="action" value="make_reservation">
                                <button class="button" formaction="CustomerController">Submit</button>
                            </form>

                        </div>

                    </div>
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

    <!-- Toggles the form to change between login/create account  -->
    <script>
        jQuery(function($) {
            $('form').validatr();
        });

        $(document).ready(function() {
            var date_input = $('input[name="Booked_Date"]'); //our date input has the name "date"
            var container = $('.bootstrap-iso form').length > 0 ? $('.bootstrap-iso form').parent() : "body";
            date_input.datepicker({
                format: 'mm/dd/yyyy',
                container: container,
                todayHighlight: true,
                autoclose: true,

            })
        })
    </script>

    <script type="text/javascript">
    </script>
    <!-- jQuery and Bootstrap scripts -->




    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.11.0/jquery.min.js"></script>
    <script>
        window.jQuery || document.write('<script src="js/jquery.min.js"><\/script>')
    </script>

    <!-- jQuery -->
    <script src="js/jquery.js"></script>

    <!-- Bootstrap Core JavaScript -->
    <script src="js/bootstrap.min.js"></script>
    <!-- Just to make our placeholder images work. Don't actually copy the next line! -->
    <script src="js/holder.min.js"></script>
    <!-- IE10 viewport hack for Surface/desktop Windows 8 bug -->
    <script src="js/ie10-viewport-bug-workaround.js"></script>
    <!-- Latest compiled and minified JavaScript -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-select/1.12.2/js/bootstrap-select.min.js"></script>

    <!-- Extra JavaScript/CSS added manually in "Settings" tab -->
    <!-- Include jQuery -->
    <script type="text/javascript" src="https://code.jquery.com/jquery-1.11.3.min.js"></script>

    <!-- Include Date Range Picker -->
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-datepicker/1.4.1/js/bootstrap-datepicker.min.js"></script>

</body>

</html>