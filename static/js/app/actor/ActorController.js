scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VActor/:idActor', {
                controller: 'VActorController',
                templateUrl: 'app/actor/VActor.html'
            }).when('/VCrearActor/:idPila', {
                controller: 'VCrearActorController',
                templateUrl: 'app/actor/VCrearActor.html'
            });
});

scrumModule.controller('VActorController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'actorService', 'identService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, actorService, identService, prodService) {
      $scope.msg = '';
      $scope.fActor = {};

      actorService.VActor({"idActor":$routeParams.idActor}).then(function (object) {
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
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };
      $scope.AElimActor3 = function(idActor) {
          
        actorService.AElimActor({"idActor":((typeof idActor === 'object')?JSON.stringify(idActor):idActor)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};

      $scope.fActorSubmitted = false;
      $scope.AModifActor0 = function(isValid) {
        $scope.fActorSubmitted = true;
        if (isValid) {
          
          actorService.AModifActor($scope.fActor).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
scrumModule.controller('VCrearActorController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'actorService', 'identService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, actorService, identService, prodService) {
      $scope.msg = '';
      $scope.fActor = {};

      actorService.VCrearActor({"idPila":$routeParams.idPila}).then(function (object) {
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
      $scope.VLogin2 = function() {
        $location.path('/VLogin');
      };

      $scope.fActorSubmitted = false;
      $scope.ACrearActor0 = function(isValid) {
        $scope.fActorSubmitted = true;
        if (isValid) {
          
          actorService.ACrearActor($scope.fActor).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
