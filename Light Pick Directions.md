# Light pick design
As of right now, I am not sure what Electronicos Fantasticos uses for their light pick.
However, I believe to have found a solution that works Good Enough for now using an IR distance sensor.
It is not perfect, but it does output sound and allows fairly accurate note selection.

## Wiring
Not much detail for now, might add a diagram eventually. For now, this is still very rough.

[This](https://www.amazon.ca/gp/product/B07D3PHQT8/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&psc=1) is the sensor I used for my pick. Many alternatives are available, they're all the same.

An IR sensor is attached to a Li-Ion battery (I used an 18650 battery) for power, and the signal output is put trhough a potentiometer (acting as a voltage divider) into a 1/4" audio jack.
Basically, treat the IR sensor as a guitar pickup with the output pin being positive and the ground pin being negative and follow any guitar volume knob wiring.


## Body

For the body, I just glued all the components to an 18650 as they felt right in my hand. VOlume knob where my finger can reach, making sure the sensor points in a good direction as to not hurt my wrist when playing.
I used a 3D pen and hot glue, since it was a pretty primitive design (although worked quite well!). Just make it comfortable in your hand and strong enough so that knobs don't break off if you push them.
