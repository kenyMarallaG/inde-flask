from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return '''
    k<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LOGIN</title>

    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <!-- SweetAlert CSS -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/sweetalert2@10">
    <!-- Font Awesome CSS -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    <!-- Your custom styles -->
    <link rel="stylesheet" href="index.css">

    <style>
        .welcome-section {
            display: none;
        }
    </style>
</head>
<body>
    <section class="vh-100 gradient-custom welcome-section">
        <div class="container py-5 h-100">
            <div class="row d-flex justify-content-center align-items-center h-100">
                <div class="col-12">
                    <h1 class="text-center text-white">Welcome to the Ferreteria Hatunsales S.A.C</h1>
                </div>
            </div>
        </div>
    </section>

    <section class="vh-100 gradient-custom">
        <div class="container py-5 h-100">
          <div class="row d-flex justify-content-center align-items-center h-100">
            <div class="col-12 col-md-8 col-lg-6 col-xl-5">
              <div class="card bg-dark text-white" style="border-radius: 1rem;">
                <div class="card-body p-5 text-center">

                  <!-- para utilizar el formgroup se debe de poner en un "form" -->
                 <form onsubmit="showWelcomeSection(); return false;">

                    <div class="mb-md-5 mt-md-4 pb-5">

                      <h2 class="fw-bold mb-2 text-uppercase">Login</h2>
                      <p class="text-white-50 mb-5">Please enter your login and password!</p>

                      <div class="form-outline form-white mb-4">
                        <input type="email" id="typeEmailX"
                          class="form-control form-control-lg" />
                        <label class="form-label" for="typeEmailX">Email</label>
                      </div>

                      <div class="form-outline form-white mb-4">
                        <input type="password" id="typePasswordX"
                          class="form-control form-control-lg" />
                        <label class="form-label" for="typePasswordX">Password</label>
                      </div>

                      <p class="small mb-5 pb-lg-2"><a class="text-white-50" href="#!">Forgot password?</a></p>

                      <button class="btn btn-outline-light btn-lg px-5" type="submit">Login</button>

                      <div class="d-flex justify-content-center text-center mt-4 pt-1">
                        <a href="#!" class="text-white"><i class="fab fa-facebook-f fa-lg"></i></a>
                        <a href="#!" class="text-white"><i class="fab fa-twitter fa-lg mx-4 px-2"></i></a>
                        <a href="#!" class="text-white"><i class="fab fa-google fa-lg"></i></a>
                      </div>

                    </div>

                  <div>
                    <p class="mb-0">Don't have an account? <a href="#!" class="text-white-50 fw-bold">Sign Up</a>
                    </p>
                  </div>

                </form>
                <!-- end del form  -->

                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

    <script>
        function showWelcomeSection() {
            document.querySelector('.welcome-section').style.display = 'block';
        }
    </script>
</body>
</html>

    '''

if __name__ == '__main__':
  app.run(debug=True)
