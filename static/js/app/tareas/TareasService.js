scrumModule.service('tareasService', ['$q', '$http', function($q, $http) {

    this.ACrearTarea = function(fTarea) {
        return  $http({
          url: "tareas/ACrearTarea",
          data: fTarea,
          method: 'POST',
        });
    //    var labels = ["/VHistoria", "/VCrearTarea", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VCrearTarea = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'tareas/VCrearTarea',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AModifTarea = function(fTarea) {
        return  $http({
          url: "tareas/AModifTarea",
          data: fTarea,
          method: 'POST',
        });
    //    var labels = ["/VHistoria", "/VCrearTarea", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.VTarea = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'tareas/VTarea',
          method: 'GET',
          params: args
        });
    //    var res = {};
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };

    this.AElimTarea = function(args) {
        if(typeof args == 'undefined') args={};
        return $http({
          url: 'tareas/AElimTarea',
          method: 'GET',
          params: args
        });
    //    var labels = ["/VHistoria", "/VTarea", ];
    //    var res = labels[0];
    //    var deferred = $q.defer();
    //    deferred.resolve(res);
    //    return deferred.promise;
    };
}]);