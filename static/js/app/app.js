// Creación del módulo de la aplicación
var scrumModule = angular.module('scrum', ['ngRoute', 'ngAnimate', 'ngTable', 'textAngular', 'flash']);
scrumModule.config(function ($routeProvider) {
    $routeProvider
        .when('/', {
                controller: 'VLoginController',
                templateUrl: 'app/ident/VLogin.html'
            });
});
scrumModule.controller('scrumController_',  ['$scope', '$http', '$location',
function($scope) {
    $scope.title = "Aplicación";
}]);
scrumModule.directive('sameAs', [function () {
    return {
        restrict: 'A',
        scope:true,
        require: 'ngModel',
        link: function (scope, elem , attrs, control) {
            var checker = function () {
                //get the value of the this field
                var e1 = scope.$eval(attrs.ngModel); 
 
                //get the value of the other field
                var e2 = scope.$eval(attrs.sameAs);
                return e1 == e2;
            };
            scope.$watch(checker, function (n) {
 
                //set the form control to valid if both 
                //fields are the same, else invalid
                control.$setValidity("unique", n);
            });
        }
    };
}]);
