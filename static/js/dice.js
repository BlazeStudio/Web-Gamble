$(document).ready(function() {
        $('#lower').click(function() {
            likeButton("lower");
        });

        $('#higher').click(function() {
            likeButton("higher");
        });

        $('#ratio').on('input', function() {
            updateMinMaxValues();
        });

        $('#bet').on('input', function() {
            updateJustPrice();
        });

    });

    function likeButton(action) {
        var ratio = document.getElementById("ratio").value;
        var bet = document.getElementById("bet").value;
        var balance = document.getElementById("balance").textContent;

        $.ajax({
            type: 'GET',
            url: '/bet',
            data: {
                action: action,
                ratio: ratio,
                bet: bet,
                balance: balance
            },
            success: function(response) {
                $('#balance').text(response.balance);
                $('#likeCount').text(response.likes);
                if (response.message.type === undefined){
                    $('#message').css("display", "none");
                }
                else if (response.message.type === "success"){
                    $('#message').removeClass('lost-message').addClass('win-message').text(response.message.text).css("display", "block");
                } else {
                    $('#message').removeClass('win-message').addClass('lost-message').text(response.message.text).css("display", "block");
                }
            },
            error: function(xhr, status, error) {
                console.error('Error:', error);
            }
        });
    }

    function updateMinMaxValues() {
        var ratio = document.getElementById("ratio").value;
        if (ratio === "") {
        $('#ratio').val(1);
        } else {
            var bet = document.getElementById("bet").value;
            var max_value = Math.round(999999 * (ratio/100))
            var min_value = Math.round((999999 * (1 - ratio / 100)));
            var maybe_win = (bet / (ratio / 100)).toFixed(2);
            $('#lower').text('0 - ' + max_value);
            $('#higher').text(min_value + ' - 999999');
            $('#value').text(maybe_win + ' ₽');
        }
    }

    function updateJustPrice() {
        var ratio = document.getElementById("ratio").value;
        var bet = document.getElementById("bet").value;
        if (bet > 99999999){
            $('#bet').val(99999999);
        }
        else{
            var maybe_win = (bet / (ratio / 100)).toFixed(2);
            $('#value').text(maybe_win + ' ₽');
        }
    }