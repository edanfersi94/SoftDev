scrumModule.service('catesService', ['$q', '$http', function($q, $http) {

    this.ACrearCategoria = function(fCategoria) {
        return  $http({
          url: "cates/ACrearCategoria",
          data: fCategoria,
          method: 'POST',
        });
    //    var labels = ["/VCategorias", "/VCategorias", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCategorias = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cates/VCategorias',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimCategoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cates/AElimCategoria',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VCategorias", "/VCategorias", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
    this.AModifCategoria = function(fCategoria) {
        return  $http({
          url: "cates/AModifCategoria",
          data: fCategoria,
          method: 'POST',
        });
    //    var labels = ["/VCategorias", "/VCategorias", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCategoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'cates/VCategoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);