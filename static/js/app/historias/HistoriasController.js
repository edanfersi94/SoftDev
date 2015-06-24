scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VHistorias/:idPila', {
                controller: 'VHistoriasController',
                templateUrl: 'app/historias/VHistorias.html'
            }).when('/VCrearHistoria/:idPila', {
                controller: 'VCrearHistoriaController',
                templateUrl: 'app/historias/VCrearHistoria.html'
            }).when('/VHistoria/:idHistoria', {
                controller: 'VHistoriaController',
                templateUrl: 'app/historias/VHistoria.html'
            }).when('/VPrioridades/:idPila', {
                controller: 'VPrioridadesController',
                templateUrl: 'app/historias/VPrioridades.html'
            }).when('/VDesempeno/:idHistoria', {
                controller: 'VDesempenoController',
                templateUrl: 'app/historias/VDesempeno.html'
            });
});

scrumModule.controller('VHistoriasController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      historiasService.VHistorias({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VHistoria0Data = $scope.res.data0;
              if(typeof VHistoria0Data === 'undefined') VHistoria0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VHistoria0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VHistoria0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VCrearHistoria1 = function(idPila) {
        $location.path('/VCrearHistoria/'+idPila);
      };
      $scope.VProducto2 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };
      $scope.VPrioridades3 = function(idPila) {
        $location.path('/VPrioridades/'+idPila);
      };
      $scope.VLogin4 = function() {
        $location.path('/VLogin');
      };

      $scope.VHistoria0 = function(idHistoria) {
        $location.path('/VHistoria/'+((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria));
      };

    }]);
scrumModule.controller('VCrearHistoriaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      $scope.fHistoria = {};

      historiasService.VCrearHistoria({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistorias0 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VCrearActor2 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion3 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo4 = function(idPila) {
        $location.path('/VCrearObjetivo/'+idPila);
      };
      $scope.VLogin5 = function() {
        $location.path('/VLogin');
      };

      $scope.fHistoriaSubmitted = false;
      $scope.ACrearHistoria1 = function(isValid) {
        $scope.fHistoriaSubmitted = true;
        if (isValid) {
          
          historiasService.ACrearHistoria($scope.fHistoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VHistoriaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'ngTableParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, ngTableParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      $scope.fHistoria = {};

      historiasService.VHistoria({"idHistoria":$routeParams.idHistoria}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VTarea2Data = $scope.res.data2;
              if(typeof VTarea2Data === 'undefined') VTarea2Data=[];
              $scope.tableParams2 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VTarea2Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VTarea2Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VHistorias3 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VLogin4 = function() {
        $location.path('/VLogin');
      };
      $scope.VCrearTarea5 = function(idHistoria) {
        $location.path('/VCrearTarea/'+idHistoria);
      };
      $scope.VCrearActor6 = function(idPila) {
        $location.path('/VCrearActor/'+idPila);
      };
      $scope.VCrearAccion7 = function(idPila) {
        $location.path('/VCrearAccion/'+idPila);
      };
      $scope.VCrearObjetivo8 = function(idPila) {
        $location.path('/VCrearObjetivo/'+idPila);
      };
      $scope.AElimHistoria9 = function(idHistoria) {
          
        historiasService.AElimHistoria({"idHistoria":((typeof idHistoria === 'object')?JSON.stringify(idHistoria):idHistoria)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VDesempeno10 = function(idHistoria) {
        $location.path('/VDesempeno/'+idHistoria);
      };

      $scope.fHistoriaSubmitted = false;
      $scope.AModifHistoria0 = function(isValid) {
        $scope.fHistoriaSubmitted = true;
        if (isValid) {
          
          historiasService.AModifHistoria($scope.fHistoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

      $scope.VTarea2 = function(idTarea) {
        $location.path('/VTarea/'+((typeof idTarea === 'object')?JSON.stringify(idTarea):idTarea));
      };

    }]);
scrumModule.controller('VPrioridadesController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      $scope.fPrioridades = {};

      historiasService.VPrioridades({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistorias1 = function(idPila) {
        $location.path('/VHistorias/'+idPila);
      };
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };

      $scope.fPrioridadesSubmitted = false;
      $scope.ACambiarPrioridades0 = function(isValid) {
        $scope.fPrioridadesSubmitted = true;
        if (isValid) {
          
          historiasService.ACambiarPrioridades($scope.fPrioridades).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VDesempenoController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'accionService', 'actorService', 'historiasService', 'identService', 'objetivoService', 'prodService', 'tareasService',
    function ($scope, $location, $route, flash, $routeParams, accionService, actorService, historiasService, identService, objetivoService, prodService, tareasService) {
      $scope.msg = '';
      historiasService.VDesempeno({"idHistoria":$routeParams.idHistoria}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VHistoria0 = function(idHistoria) {
        $location.path('/VHistoria/'+idHistoria);
      };

    }]);
