scrumModule.service('prodService', ['$q', '$http', function($q, $http) {

    this.VProductos = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'prod/VProductos',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AModifProducto = function(fPila) {
        return  $http({
          url: "prod/AModifProducto",
          data: fPila,
          method: 'POST',
        });
    //    var labels = ["/VProductos", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VProducto = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'prod/VProducto',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearProducto = function(fPila) {
        return  $http({
          url: "prod/ACrearProducto",
          data: fPila,
          method: 'POST',
        });
    //    var labels = ["/VProductos", "/VCrearProducto", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearProducto = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'prod/VCrearProducto',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);