scrumModule.config(function ($routeProvider) {
    $routeProvider.when('/VMaestroScrum', {
                controller: 'VMaestroScrumController',
                templateUrl: 'app/mast/VMaestroScrum.html'
            });
});

scrumModule.controller('VMaestroScrumController', 
   ['$scope', '$location', '$route', 'flash', 'identService', 'mastService',
    function ($scope, $location, $route, flash, identService, mastService) {
      $scope.msg = '';
      mastService.VMaestroScrum().then(function (object) {
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
