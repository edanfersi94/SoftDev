scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VObjetivo/:idObjetivo', {
                controller: 'VObjetivoController',
                templateUrl: 'app/objetivo/VObjetivo.html'
            }).when('/VCrearObjetivo/:idPila', {
                controller: 'VCrearObjetivoController',
                templateUrl: 'app/objetivo/VCrearObjetivo.html'
            });
});

scrumModule.controller('VObjetivoController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, objetivoService, prodService) {
      $scope.msg = '';
      $scope.fObjetivo = {};

      objetivoService.VObjetivo({"idObjetivo":$routeParams.idObjetivo}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VProducto1 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.fObjetivoSubmitted = false;
      $scope.AModifObjetivo0 = function(isValid) {
        $scope.fObjetivoSubmitted = true;
        if (isValid) {
          
          objetivoService.AModifObjetivo($scope.fObjetivo).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VCrearObjetivoController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'objetivoService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, objetivoService, prodService) {
      $scope.msg = '';
      $scope.fObjetivo = {};

      objetivoService.VCrearObjetivo({"idPila":$routeParams.idPila}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VProducto1 = function(idPila) {
        $location.path('/VProducto/'+idPila);
      };

      $scope.fObjetivoSubmitted = false;
      $scope.ACrearObjetivo0 = function(isValid) {
        $scope.fObjetivoSubmitted = true;
        if (isValid) {
          
          objetivoService.ACrearObjetivo($scope.fObjetivo).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
