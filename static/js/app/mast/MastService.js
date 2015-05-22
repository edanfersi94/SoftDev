scrumModule.service('mastService', ['$q', '$http', function($q, $http) {

    this.VMaestroScrum = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'mast/VMaestroScrum',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);