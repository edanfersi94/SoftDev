scrumModule.service('accionService', ['$q', '$http', function($q, $http) {

    this.AModifAccion = function(fAccion) {
        return  $http({
          url: "accion/AModifAccion",
          data: fAccion,
          method: 'POST',
        });
    //    var labels = ["/VProducto", "/VAccion", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VAccion = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'accion/VAccion',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimAccion = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'accion/AElimAccion',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VProducto", "/VAccion", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.VCrearAccion = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'accion/VCrearAccion',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearAccion = function(fAccion) {
        return  $http({
          url: "accion/ACrearAccion",
          data: fAccion,
          method: 'POST',
        });
    //    var labels = ["/VProducto", "/VCrearAccion", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);