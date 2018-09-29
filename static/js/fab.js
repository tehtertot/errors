document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.fixed-action-btn');
    options = {
        'direction': 'right'
    }
    var instances = M.FloatingActionButton.init(elems, options);
  });