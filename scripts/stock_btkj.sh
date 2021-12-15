### stock
python -u main_informer.py --model informer --root_path ./data/Stock --data custom --features MS --seq_len 48 --label_len 48 --pred_len 24 --e_layers 2 --d_layers 1 --attn prob --des 'Exp' --itr 5 --factor 3 --do_predict
