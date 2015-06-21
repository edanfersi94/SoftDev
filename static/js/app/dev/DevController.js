scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VDesarrollador', {
                controller: 'VDesarrolladorController',
                templateUrl: 'app/dev/VDesarrollador.html'
            });
});

scrumModule.controller('VDesarrolladorController', 
   ['$scope', '$location', '$route', 'flash', 'devService', 'identService',
    function ($scope, $location, $route, flash, devService, identService) {
      $scope.msg = '';
      devService.VDesarrollador().then(function (object) {
        $scope.res = object.data;
        for (var key in object.data) {
            $scope[key] = object.data[key];
        }
        if ($scope.logout) {
            $location.path('/');
        }
      });
      $scope.VLogin0 = function() {
        $location.path('/VLogin');
      };

    }]);
