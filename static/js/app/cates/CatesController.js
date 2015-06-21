scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VCategorias', {
                controller: 'VCategoriasController',
                templateUrl: 'app/cates/VCategorias.html'
            }).when('/VCategoria/:idCategoria', {
                controller: 'VCategoriaController',
                templateUrl: 'app/cates/VCategoria.html'
            });
});

scrumModule.controller('VCategoriasController', 
   ['$scope', '$location', '$route', 'flash', 'ngTableParams', 'catesService', 'identService', 'prodService',
    function ($scope, $location, $route, flash, ngTableParams, catesService, identService, prodService) {
      $scope.msg = '';
      $scope.fCategoria = {};

      catesService.VCategorias().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
              var VCategoria0Data = $scope.res.data0;
              if(typeof VCategoria0Data === 'undefined') VCategoria0Data=[];
              $scope.tableParams0 = new ngTableParams({
                  page: 1,            // show first page
                  count: 10           // count per page
              }, {
                  total: VCategoria0Data.length, // length of data
                  getData: function($defer, params) {
                      $defer.resolve(VCategoria0Data.slice((params.page() - 1) * params.count(), params.page() * params.count()));
                  }
              });            


      });
      $scope.VProductos2 = function() {
        $location.path('/VProductos');
      };
      $scope.VLogin3 = function() {
        $location.path('/VLogin');
      };

      $scope.fCategoriaSubmitted = false;
      $scope.ACrearCategoria1 = function(isValid) {
        $scope.fCategoriaSubmitted = true;
        if (isValid) {
          
          catesService.ACrearCategoria($scope.fCategoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

      $scope.VCategoria0 = function(idCategoria) {
        $location.path('/VCategoria/'+((typeof idCategoria === 'object')?JSON.stringify(idCategoria):idCategoria));
      };

    }]);
scrumModule.controller('VCategoriaController', 
   ['$scope', '$location', '$route', 'flash', '$routeParams', 'catesService', 'identService', 'prodService',
    function ($scope, $location, $route, flash, $routeParams, catesService, identService, prodService) {
      $scope.msg = '';
      $scope.fCategoria = {};

      catesService.VCategoria({"idCategoria":$routeParams.idCategoria}).then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.AElimCategoria0 = function(idCategoria) {
          
        catesService.AElimCategoria({"idCategoria":((typeof idCategoria === 'object')?JSON.stringify(idCategoria):idCategoria)}).then(function (object) {
          var msg = object.data["msg"];
          if (msg) flash(msg);
          var label = object.data["label"];
          $location.path(label);
          $route.reload();
        });};
      $scope.VCategorias2 = function() {
        $location.path('/VCategorias');
      };
      $scope.VLogin3 = function() {
        $location.path('/VLogin');
      };

      $scope.fCategoriaSubmitted = false;
      $scope.AModifCategoria1 = function(isValid) {
        $scope.fCategoriaSubmitted = true;
        if (isValid) {
          
          catesService.AModifCategoria($scope.fCategoria).then(function (object) {
              var msg = object.data["msg"];
              if (msg) flash(msg);
              var label = object.data["label"];
              $location.path(label);
              $route.reload();
          });
        }
      };

    }]);
