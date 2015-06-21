scrumModule.service('objetivoService', ['$q', '$http', function($q, $http) {

    this.AModifObjetivo = function(fObjetivo) {
        return  $http({
          url: "objetivo/AModifObjetivo",
          data: fObjetivo,
          method: 'POST',
        });
    //    var labels = ["/VProducto", "/VObjetivo", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VObjetivo = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'objetivo/VObjetivo',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearObjetivo = function(fObjetivo) {
        return  $http({
          url: "objetivo/ACrearObjetivo",
          data: fObjetivo,
          method: 'POST',
        });
    //    var labels = ["/VProducto", "/VCrearObjetivo", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearObjetivo = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'objetivo/VCrearObjetivo',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimObjetivo = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'objetivo/AElimObjetivo',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VProducto", "/VObjetivo", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);