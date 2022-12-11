import edifice as ed
from LCM_recive import Recived_pod_data
from Dashboard_style import *


class Nirman_dashboard(ed.Component):
    def __init__(self):
        super().__init__()
        self.acceleration = 0
        self.velocity = 0
        self.height = 0
        self.high_vol = 0
        self.low_vol = 0

        self.worker = Recived_pod_data()
        self.worker.start()
        self.worker.update_acceleration.connect(self.setacc)
        self.worker.update_velocity.connect(self.setvel)
        self.worker.update_height.connect(self.sethgt)
        self.worker.update_h_vol.connect(self.set_h_vol)
        self.worker.update_l_vol.connect(self.set_l_vol)


        self.pod_acc = ed.StateValue(self.acceleration)
        self.pod_vel = ed.StateValue(self.velocity)
        self.pod_hgt = ed.StateValue(self.height)
        self.pod_h_vol = ed.StateValue(self.high_vol)
        self.pod_l_vol = ed.StateValue(self.low_vol)

    def setacc(self, value):
        self.pod_acc.set(value)
    def setvel(self, value):
        self.pod_vel.set(value)
    def sethgt(self, value):
        self.pod_hgt.set(value)
    def set_h_vol(self, value):
        self.pod_h_vol.set(value)
    def set_l_vol(self, value):
        self.pod_l_vol.set(value)


    def render(self):
        acceleration = self.pod_acc.subscribe(self)
        velocity = self.pod_vel.subscribe(self)
        height = self.pod_hgt.subscribe(self)
        high_vol = self.pod_h_vol.subscribe(self)
        low_vol = self.pod_l_vol.subscribe(self)

        
        return ed.Window(title="Hyperloop Dashboard")(
            ed.View(layout='row', style={"margin": 50,"height":600,"width":1000,"background":main_background})(
                ed.View(layout="column")(
                    ed.View(layout="column",style= widgit_style)(
                        ed.Label(text="Acceleration", style=tag_style),
                        ed.View(style=data_background_style)(ed.Label(text=acceleration,style=data_style)),
                        ed.Label(text="m/s\u00b2", style=data_unit_style),
                        ed.View(layout="row",style = slider_background)(
                            ed.View(layout="row",style = {"border-radius": 10,"width":(acceleration*3.6),"height":25,"background":"#05d4e4"})())),

                    ed.View(layout="column",style= widgit_style)(
                        ed.Label(text="Velocity", style=tag_style),
                        ed.View(style=data_background_style)(ed.Label(text=velocity,style=data_style)),
                        ed.Label(text="m/s", style=data_unit_style),
                        ed.View(layout="row",style = slider_background)(
                            ed.View(layout="row",style = {"border-radius": 10,"width":(velocity*3.6),"height":25,"background":"#05d4e4"})())),

                    ed.View(layout="column",style= widgit_style)(
                        ed.Label(text="Pod Height", style=tag_style),
                        ed.View(style=data_background_style)(ed.Label(text=height,style=data_style)),
                        ed.Label(text="cm", style=data_unit_style),
                        ed.View(layout="row",style = slider_background)(
                            ed.View(layout="row",style = {"border-radius": 10,"width":(height*36),"height":25,"background":"#05d4e4"})()))
                ),
                ed.View(layout="column",style={"margin":50})(
                    ed.View(layout="column",style= right_widgit_style)(
                        ed.Label(text="Main_Battery",style = right_tag_style),
                        ed.View(style=right_data_background_style)(ed.Label(text=f"{high_vol} V",style=data_style))
                    ),
                    ed.View(layout="column",style= right_widgit_style)(
                        ed.Label(text="Control_Battery",style = right_tag_style),
                        ed.View(style=right_data_background_style)(ed.Label(text=f"{low_vol} V",style=data_style))
                    )
                )
                    

                
            ))


if __name__ == "__main__":
    ed.App(Nirman_dashboard()).start()