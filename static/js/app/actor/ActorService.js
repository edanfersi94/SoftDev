scrumModule.service('actorService', ['$q', '$http', function($q, $http) {

    this.AModifActor = function(fActor) {
        return  $http({
          url: "actor/AModifActor",
          data: fActor,
          method: 'POST',
        });
    //    var labels = ["/VProducto", "/VActor", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VActor = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'actor/VActor',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearActor = function(fActor) {
        return  $http({
          url: "actor/ACrearActor",
          data: fActor,
          method: 'POST',
        });
    //    var labels = ["/VProducto", "/VCrearActor", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearActor = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'actor/VCrearActor',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimActor = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'actor/AElimActor',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VProducto", "/VActor", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);