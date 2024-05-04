
    let timerInterval;
    let startTime;

    function startTimer() {
      startTime = Date.now();
      timerInterval = setInterval(updateTimer, 1000);
    }

    function stopTimer() {
      clearInterval(timerInterval);
    }

    function updateTimer() {
      const elapsedTime = Date.now() - startTime;
      const seconds = Math.floor(elapsedTime / 1000);
      const minutes = Math.floor(seconds / 60);
      const hours = Math.floor(minutes / 60);

      const displaySeconds = seconds % 60;
      const displayMinutes = minutes % 60;
      const displayHours = hours % 24;

      const formattedTime = `${displayHours.toString().padStart(2, '0')}:${displayMinutes.toString().padStart(2, '0')}:${displaySeconds.toString().padStart(2, '0')}`;
      document.getElementById('timer').textContent = formattedTime;
    }

    document.getElementById('startButton').addEventListener('click', startTimer);
    document.getElementById('stopButton').addEventListener('click', stopTimer);

    // Stop timer when leaving the page
    window.addEventListener('beforeunload', function(event) {
      if (timerInterval) {
        stopTimer();
      }
    });
