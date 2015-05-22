scrumModule.service('devService', ['$q', '$http', function($q, $http) {

    this.VDesarrollador = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'dev/VDesarrollador',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);