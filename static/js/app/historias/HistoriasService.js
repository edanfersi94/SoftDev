scrumModule.service('historiasService', ['$q', '$http', function($q, $http) {

    this.VHistorias = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VHistorias',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.ACrearHistoria = function(fHistoria) {
        return  $http({
          url: "historias/ACrearHistoria",
          data: fHistoria,
          method: 'POST',
        });
    //    var labels = ["/VHistorias", "/VCrearHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VCrearHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AModifHistoria = function(fHistoria) {
        return  $http({
          url: "historias/AModifHistoria",
          data: fHistoria,
          method: 'POST',
        });
    //    var labels = ["/VHistorias", "/VHistoria", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VHistoria = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'historias/VHistoria',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

}]);